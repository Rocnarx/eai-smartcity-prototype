# 🏙️ EAI Smart City Prototype

Prototype REST API developed as part of the research project:

> **“Integration of Digital Urban Services through Open-Source EAI Platforms in Smart Cities.”**

---

## 🧭 Overview

This prototype provides a **base environment for testing interoperability** between digital urban services, such as:

- 🛒 Commerce (store orders)
- 🚚 Transport coordination
- 💬 Messaging and notifications

It was developed in **Python + FastAPI** and deployed on **Railway.app** to provide a publicly accessible API for experimentation and validation of integration flows.

---

## ⚙️ Technical Stack

| Component | Description |
|------------|--------------|
| **Language** | Python 3.10+ |
| **Framework** | FastAPI |
| **Server** | Uvicorn (ASGI) |
| **Deployment** | Railway.app (PaaS) |
| **Integration Context** | EAI / Smart City prototype |
| **Architecture Type** | RESTful API |

---

## 🌐 Public Deployment

Once deployed on Railway, the service will be accessible through a URL similar to:

```
https://eai-smartcity-prototype.up.railway.app
```

You can verify that the server is running using:

```
GET /api/status
```

Response:
```json
{
  "status": "ok",
  "message": "Servidor en línea 🚀"
}
```

---

## 🧩 Endpoints

| Method | Endpoint | Description | Example Payload |
|---------|-----------|--------------|-----------------|
| `GET` | `/api/status` | Health check for the server | — |
| `POST` | `/api/tienda` | Simulates an order from a store | `{ "cliente": "Juan", "valor": 120.5 }` |
| `POST` | `/api/mensajeria` | Simulates sending a notification message | `{ "destino": "Juan", "contenido": "Pedido entregado" }` |

---

## 🚀 Local Execution

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-user>/eai-smartcity-prototype.git
   cd eai-smartcity-prototype
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run locally:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

4. Open your browser:
   ```
   http://localhost:8000/docs
   ```

---

## 🧱 Deployment on Railway

1. Push the repository to GitHub.  
2. Go to [Railway.app](https://railway.app) → **New Project → Deploy from GitHub Repo**.  
3. Set the **Start Command** to:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
4. Click **Deploy**.  
5. Railway will generate a public HTTPS URL.

---

## 🧠 Research Context

This API prototype serves as a **practical foundation** for evaluating **EAI open-source platforms** such as:

- n8n (Low-Code Orchestration)
- Apache Camel (Enterprise Integration Patterns)
- RabbitMQ / Kafka (Event-Driven Messaging)

It validates the first step of the research objective:
> *“Demonstrate that open-source EAI tools can integrate heterogeneous digital services in smart city contexts without modifying their core systems.”*

---

## 📄 License

MIT License © 2025 — Research Project at Universidad Distrital Francisco José de Caldas  
Developed by Christian Camilo Lancheros Sánchez under the direction of **Prof. José Joaquín Bocanegra García**.

---

## 🧩 Citation

If this project is referenced in an academic context, please cite as:

---