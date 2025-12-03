import pyautogui

pyautogui.press('Win') # usado para prescionar uma tecla desejada
pyautogui.sleep(1) # usado para ajustar o tempo de execucao entre uma ordem e outra
pyautogui.write('Gogle Chrome', interval = 0.2) # utilizado para escrever
pyautogui.press('Enter')
pyautogui.sleep(1)
pyautogui.write('Senai - Santana de Parnaíba', interval = 0.1)
pyautogui.press('Enter')
pyautogui.sleep(1)
pyautogui.moveTo(906,507, duration=0.4) # utilizado para mover o mouse nas coordenadas de X e Y
pyautogui.click()
pyautogui.sleep(1)
pyautogui.hotkey('shift', 'win', 's')
pyautogui.sleep(1)
pyautogui.moveTo(811,226, duration=0.5)

pyautogui.mouseDown()
pyautogui.moveTo(1751, 1825, duration=0.5)
pyautogui.mouseUp()
pyautogui.sleep(2)
pyautogui.press('win')
pyautogui.sleep(1)
pyautogui.write('Paint', interval=0.2)
pyautogui.press('Enter')
pyautogui.sleep(2)
pyautogui. hotkey('ctrl', 'v')