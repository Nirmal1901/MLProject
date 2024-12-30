# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /streamlit

# Copy files to the container
COPY . /streamlit

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "streamlit_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
