import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

class SudokuSolver:
  def __init__(self, sudoku, model):
    self.making_array(sudoku)
    self.model = model
  def making_array(self, img_path):
      self.img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
      self.img = cv2.resize(self.img[14:-14, 14:-14], (1008, 1008))
      self.cell_size = 1008 // 9
      self.cells = []
      for row in range(9):
          for col in range(9):
              cell = self.img[row * self.cell_size:(row + 1) * self.cell_size, col * self.cell_size:(col + 1) * self.cell_size]
              t = cv2.equalizeHist(cell)
              self.cells.append(t)
      self.arr = np.array(self.cells)

  def checkIFNotblank(self, pxl,arr):
      if np.mean(arr[pxl,30:80, 30:80]) < 250:
          return True
      return False

  def detect_digit(self, image_array):
      resized_image = cv2.resize(image_array, (90, 90))
      normalized_image = resized_image / 255.0
      reshaped_image = normalized_image.reshape(1, 28, 28, 1)
      predictions = self.model.predict(reshaped_image)
      return np.argmax(predictions)

  def create_matrix(self, images_array):
      results = []
      for i, image in enumerate(images_array):
        if self.checkIFNotblank(i, images_array):
          results.append(self.detect_digit(images_array[i, 8:100 ,20:110]))
        else:
          results.append(0)
      self.matrix_9x9 = np.array(results).reshape(9, 9)
      self.matrix_9x9 = self.matrix_9x9.astype(int)
      self.solve(self.matrix_9x9)


  def give(self):
    self.create_matrix(self.arr)
    self.draw_sudoku(self.matrix_9x9)
    return self.drawn_img
  def solve(self, bo):
    find = self.find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if self.valid(bo, i, (row, col)):
            bo[row][col] = i

            if self.solve(bo):
                return True

            bo[row][col] = 0

    return False


  def valid(self, bo, num, pos):
      for i in range(len(bo[0])):
          if bo[pos[0]][i] == num and pos[1] != i:
              return False
      for i in range(len(bo)):
          if bo[i][pos[1]] == num and pos[0] != i:
              return False

      box_x = pos[1] // 3
      box_y = pos[0] // 3

      for i in range(box_y*3, box_y*3 + 3):
          for j in range(box_x * 3, box_x*3 + 3):
              if bo[i][j] == num and (i,j) != pos:
                  return False
      return True

  def find_empty(self,bo):
      for i in range(len(bo)):
          for j in range(len(bo[0])):
              if bo[i][j] == 0:
                  return i, j

      return None
  def save(self):
      self.drawn_img.save("Generated_Sudoku.png")
  def draw_sudoku(self, sudoku, cell_size=70):
    img_size = cell_size * 9
    self.drawn_img = Image.new("RGB", (img_size, img_size), "white")
    draw = ImageDraw.Draw(self.drawn_img)
    for i in range(10):
        width = 3 if i % 3 == 0 else 1
        draw.line([(0, i * cell_size), (img_size, i * cell_size)], fill="black", width=width)
        draw.line([(i * cell_size, 0), (i * cell_size, img_size)], fill="black", width=width)
    font = ImageFont.truetype("ARIAL.TTF", cell_size//2)
    for i in range(9):
        for j in range(9):
            draw.text((j * cell_size + cell_size//3, i * cell_size + cell_size//3), str(sudoku[i][j]), fill=(3, 127, 252), font = font)

