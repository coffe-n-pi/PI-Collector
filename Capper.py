import cv2

class Capper():
  def __init__(self):
    # Capture device
    self.cap_dev = cv2.VideoCapture(0)

    #video_FourCC    = int(vid.get(cv2.CAP_PROP_FOURCC))
    #video_fps       = vid.get(cv2.CAP_PROP_FPS)
    #video_size      = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
    #                   int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
  def GetImage(self):
    _, frame = self.cap_dev.read()
    _, img_encoded = cv2.imencode('.jpg', frame)
    return img_encoded
