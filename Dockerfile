# Use an official Python runtime as a parent image
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y binutils libglib2.0-0 libsm6 libxext6 libxrender1 libfontconfig1 \
                       libxkbcommon0 libwayland-cursor0 libwayland-client0 libdbus-1-3 \
                       libxcb-xinerama0 libxcb-icccm4 libxcb-randr0 libx11-xcb1 libxkbcommon-x11-0 \
                       libxcb-xkb1 libxcb-sync1 libxcb-render0 libxcb-shape0 libxcb-xfixes0 \
                       libxcb-render-util0 libxcomposite1 libwayland-egl1 libxcb-keysyms1 \
                       libxcb-glx0 libxcb-image0 libxcb-util1 libxcb-shm0 libqt5gui5 \
                       libqt5core5a libqt5widgets5 libcairo-gobject2 libatk1.0-0 libpango-1.0-0 \
                       libgtk-3-0 libcairo2 libpangocairo-1.0-0 libgdk-pixbuf2.0-0

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install pyinstaller

# Install Flask and specific versions of dependencies
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["pyinstaller", "--onefile", "--windowed", "--icon=logo.ico", "YoutubeDownloader.py"]