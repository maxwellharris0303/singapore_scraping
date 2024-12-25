import logo from "./logo.svg";
import "./App.css";
import { Button, Col, Space, Input } from "antd";
import axios from "axios";
import { useState } from "react";

function App() {
  const handleScraping = () => {
    const fetchData = async () => {
      try {
        const response = await axios.post(
          "http://65.21.88.226:82/schedule-scraping"
        );
        const responseData = response.data;
        console.log(response, responseData);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData();
  };
  const handleRunBot = () => {
    const fetchData1 = async () => {
      try {
        const response = await axios.post("http://65.21.88.226:83/run-bot");
        const responseData = response.data;
        console.log(response, responseData);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData1();
  };
  const handleTest = () => {
    const fetchData2 = async () => {
      try {
        const response = await axios.post("http://65.21.88.226:84/test-bot");
        const responseData = response.data;
        console.log(response, responseData);
      } catch (error) {
        console.error(error);
      }
    };
    fetchData2();
  };

  return (
    <div className="App">
      <header className="App-header">
        <Space size="large">
          <Button type="primary" size="large" onClick={handleScraping}>
            Schedule Scraping
          </Button>
          <Button type="primary" size="large" onClick={handleRunBot}>
            Run Bot
          </Button>
          <Button type="dashed" size="large" onClick={handleTest}>
            Test
          </Button>
        </Space>
      </header>
    </div>
  );
}

export default App;
