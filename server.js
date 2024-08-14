// server.js or app.js
const PORT = process.env.PORT || 8080;

// Your server setup code here, e.g., Express server
const express = require('express');
const app = express();

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
