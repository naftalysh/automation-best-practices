const express = require('express');
const router = express.Router();
const os = require('os');

// Basic health check endpoint
router.get('/', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    version: process.env.npm_package_version || '1.0.0'
  });
});

// Detailed health check with system info
router.get('/details', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    version: process.env.npm_package_version || '1.0.0',
    memory: {
      free: os.freemem(),
      total: os.totalmem(),
      usage: process.memoryUsage()
    },
    cpu: {
      load: os.loadavg(),
      cores: os.cpus().length
    },
    hostname: os.hostname(),
    platform: os.platform(),
    nodeVersion: process.version
  });
});

// Database health check
router.get('/db', async (req, res) => {
  try {
    // Check if mongoose is connected
    const mongoose = require('mongoose');
    const isConnected = mongoose.connection.readyState === 1;

    if (isConnected) {
      res.status(200).json({
        status: 'healthy',
        database: 'connected',
        timestamp: new Date().toISOString()
      });
    } else {
      res.status(503).json({
        status: 'unhealthy',
        database: 'disconnected',
        timestamp: new Date().toISOString()
      });
    }
  } catch (error) {
    res.status(500).json({
      status: 'error',
      message: error.message,
      timestamp: new Date().toISOString()
    });
  }
});

module.exports = router;
