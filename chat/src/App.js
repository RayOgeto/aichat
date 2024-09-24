import React, { useState } from "react";
import './App.css';

const App = () => {
  const [messages, setMessages] = useState([]);  // Store chat messages
  const [input, setInput] = useState("");        // Input for new message

  // Function to send a message
  const handleSendMessage = async () => {
    if (input.trim()) {
      const userMessage = { text: input, sender: "user" };
      setMessages([...messages, userMessage]);

      // Send symptoms to the backend to diagnose malaria
      const botResponse = await fetchMalariaDiagnosis(input);
      setMessages(prevMessages => [...prevMessages, { text: botResponse, sender: "bot" }]);

      setInput(""); // Clear input after sending
    }
  };

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  // Call the backend to diagnose malaria based on symptoms
  const fetchMalariaDiagnosis = async (symptoms) => {
    const response = await fetch("http://localhost:5000/diagnose", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ symptoms })
    });
    const data = await response.json();
    return data.diagnosis;  // Return the diagnosis response
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.sender}`}>
            {message.text}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          placeholder="Enter your symptoms..."
          className="chat-input"
        />
        <button onClick={handleSendMessage} className="send-button">
          Send
        </button>
      </div>
    </div>
  );
};

export default App;
