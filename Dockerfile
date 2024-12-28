# Base Image
FROM python:3.9-slim

# Set working directory
WORKDIR /app
ENV PYTHONPATH=/app

# Copy application code
COPY app /app

RUN mkdir -p .streamlit
COPY /app/web/.streamlit/config.toml .streamlit/config.toml


# Install dependencies
COPY requirements.txt .
RUN pip install --use-deprecated=legacy-resolver --no-cache-dir -r requirements.txt

# Verify that the file exists (optional debugging step)
RUN echo "Files in /app:"
RUN ls -la /app
RUN echo "Files in /app/web:"
RUN ls -la /app/web

# Expose port for Streamlit
EXPOSE 8501

# Expose port 9000 for FastAPI
EXPOSE 8502

# Start both FastAPI and Streamlit
CMD uvicorn main:app --host 0.0.0.0 --port 8502 & \
    streamlit run web/ai-assistant-web.py --server.port 8501 --server.address 0.0.0.0
