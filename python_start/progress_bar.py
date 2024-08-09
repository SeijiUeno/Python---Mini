import time

def ft_progress(lst):
  start_time = time.time()
  total_items = len(lst)
  bar_length = 20
  for i, item in enumerate(lst, 1):
    elapsed_time = time.time() - start_time
    percent_completed = i / total_items * 100
    eta = elapsed_time / percent_completed * (100 - percent_completed)
    filled_length = int(percent_completed / 100 * bar_length)
    bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length - 1)
    print(f'ETA: {eta:.2f}s [{percent_completed:03.0f}%][{bar}] {i}/{total_items} | elapsed time {elapsed_time:.2f}s', end='\r')
    yield item

