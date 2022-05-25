from progressbar import ProgressBar

pbar = ProgressBar().start()
def job():
   total_steps = 7
    # script 1
    pbar.update((1.01/)*100)  # current step/total steps * 100
    # script 2
    pbar.update((2/7)*100)  # current step/total steps * 100
    # ....
    pbar.finish()

pow(1.01,500)
