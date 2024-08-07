# Project-CE4-32dot
32dot🕺

32dot은 Google의 MediaPipe Pose Landmark Detection을 이용해 만들어진 프로그램으로, 웹캠으로 사용자의 동작을 촬영하고 포즈 데이터를 동작을 비교할 영상의 데이터와 비교해 정확도를 계산합니다. 32dot의 이름은 Pose Landmark를 32개의 점으로 표현한다는 점에서 착안되었습니다. 또한 오늘 행사에 참가한 부스 중 가장 높은 기술적 난이도를 자랑하는 프로그램입니다.

32dot은 Python을 사용하여 카메라로 사용자의 동작을 캡처하고, 미리 녹화된 영상과 비교하여 유사성을 측정하는 머신러닝 프로그램입니다. 이 프로젝트는 여러 가지 라이브러리와 머신러닝 기술을 결합하여 만들어졌습니다.

OpenCV와 Mediapipe를 사용하여 카메라로부터 영상을 실시간으로 캡처하고, 포즈 랜드마크를 추출, 저장합니다. NumPy를 사용해 저장된 포즈 랜드마크와 레퍼런스가 될 랜드마크를 비교하고, cosine similarity를 사용하여 유사성을 측정하고, tkinter를 사용하여 최종 결과를 표시합니다.

PPT: https://www.canva.com/design/DAFxn69JfKY/2bXz91fXNdldb8suhSOwYQ/view?utm_content=DAFxn69JfKY&utm_campaign=designshare&utm_medium=link&utm_source=editor
