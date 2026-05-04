import cv2

def capture_video(source=0):
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Không mở được video")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (1280, 720))

        cv2.imshow("Capture", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_video("video.mp4")  # hoặc 0
