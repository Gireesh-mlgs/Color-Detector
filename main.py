import cv2
import webcolors
from math import sqrt

def closest_color(rgb):
    min_distance = float("inf")
    closest_name = "Unknown"

    for hex_code, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(hex_code)

        distance = sqrt(
            (rgb[0] - r) ** 2 +
            (rgb[1] - g) ** 2 +
            (rgb[2] - b) ** 2
        )

        if distance < min_distance:
            min_distance = distance
            closest_name = name

    return closest_name

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    h, w = frame.shape[:2]
    cx, cy = w // 2, h // 2

    b, g, r = frame[cy, cx]

    color_name = closest_color((r, g, b))

    cv2.drawMarker(
        frame,
        (cx, cy),
        (255, 255, 255),
        cv2.MARKER_CROSS,
        20,
        2,
    )

    cv2.rectangle(frame, (10, 10), (340, 120), (40, 40, 40), -1)

    cv2.rectangle(
        frame,
        (250, 20),
        (320, 90),
        (int(b), int(g), int(r)),
        -1,
    )

    cv2.putText(
        frame,
        f"Color: {color_name.title()}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
    )

    cv2.putText(
        frame,
        f"RGB: ({r}, {g}, {b})",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2,
    )

    cv2.putText(
        frame,
        "Press Q to Quit",
        (20, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (200, 200, 200),
        1,
    )

    cv2.imshow("Live Color Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
