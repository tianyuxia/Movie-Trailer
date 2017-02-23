import webbrowser
import time

total_break = 3
break_count = 0

while(break_count < total_break):
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=ZmuGk-wwajE")
    break_count += 1