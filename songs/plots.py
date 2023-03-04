import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
  buffer = BytesIO()
  plt.savefig(buffer, format="png")
  buffer.seek(0)
  img = buffer.getvalue()
  g = base64.b64encode(img)
  g = g.decode("utf-8")
  buffer.close()
  return g

def bar_plot(x, h, arr):
  plt.figure(figsize=(2,2))
  plt.yticks(range(min(arr), max(arr)+1))
  plt.xticks(rotation=90)
  plt.bar(x,h, width=0.4)
  return get_graph()