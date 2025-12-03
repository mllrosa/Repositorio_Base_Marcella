import pyautogui 

for i in range(10):
    # Movendo o mouse em um quadrado que se move
    pyautogui.moveTo(100 + 10 * i, 100 + 10 * i, duration=0.25) # 'moveTo' indica a onde o mouse deve se mover
    pyautogui.moveTo(200 + 10 * i, 100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i, 200 + 10 * i, duration=0.25)
    pyautogui.moveTo(100 + 10 * i, 200 + 10 * i, duration=0.25)