const request = require('supertest');
const { app } = require('../src/server');

describe('Health API', () => {
  describe('GET /health', () => {
    it('should return healthy status', async () => {
      const res = await request(app).get('/health');
      
      expect(res.statusCode).toEqual(200);
      expect(res.body.status).toBe('healthy');
      expect(res.body).toHaveProperty('timestamp');
      expect(res.body).toHaveProperty('uptime');
      expect(res.body).toHaveProperty('version');
    });
  });

  describe('GET /health/details', () => {
    it('should return detailed health information', async () => {
      const res = await request(app).get('/health/details');
      
      expect(res.statusCode).toEqual(200);
      expect(res.body.status).toBe('healthy');
      expect(res.body).toHaveProperty('timestamp');
      expect(res.body).toHaveProperty('uptime');
      expect(res.body).toHaveProperty('version');
      expect(res.body).toHaveProperty('memory');
      expect(res.body).toHaveProperty('cpu');
      expect(res.body).toHaveProperty('hostname');
      expect(res.body).toHaveProperty('platform');
      expect(res.body).toHaveProperty('nodeVersion');
    });
  });
});
