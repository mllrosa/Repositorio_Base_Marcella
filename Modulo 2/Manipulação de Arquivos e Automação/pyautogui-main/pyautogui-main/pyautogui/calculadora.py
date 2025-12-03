import pyautogui

pyautogui.hotkey('Win', 'r') # ''hotkey ´´e para combinar teclas
pyautogui.sleep(1)
pyautogui.write('calc')
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.press('8')
pyautogui.sleep(2)
pyautogui.press('+')
pyautogui.sleep(2)
pyautogui.press('2')
pyautogui.press('=')

print(" O calculo foi realizado na calculadora do Windows.")
print("Confira o histórico da calculadora")