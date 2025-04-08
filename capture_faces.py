import cv2
import os

DATASET_DIR = "dataset"

def capture_faces():
    cam = cv2.VideoCapture(0)
    name = input("Enter person's name: ").strip()

    if not name:
        print("❌ Name cannot be empty.")
        return

    person_dir = os.path.join(DATASET_DIR, name)
    os.makedirs(person_dir, exist_ok=True)

    print("[INFO] Press 'c' to capture, 'q' to quit.")

    img_count = len(os.listdir(person_dir))

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        cv2.imshow(f"Capturing: {name}", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            img_name = f"{name}_{img_count + 1}.jpg"
            img_path = os.path.join(person_dir, img_name)
            cv2.imwrite(img_path, frame)
            img_count += 1
            print(f"[CAPTURED] {img_path}")

        elif key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"[DONE] {img_count} images saved to {person_dir}")

if __name__ == "__main__":
    capture_faces()
