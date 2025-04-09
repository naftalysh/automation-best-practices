const request = require('supertest');
const mongoose = require('mongoose');
const { app, startServer } = require('../src/server');
const Product = require('../src/models/productModel');

// Mock the mongoose connect method
jest.mock('mongoose', () => {
  const originalModule = jest.requireActual('mongoose');
  return {
    ...originalModule,
    connect: jest.fn().mockResolvedValue(true)
  };
});

describe('Product API', () => {
  let server;

  beforeAll(async () => {
    // Start the server for testing
    server = await startServer();
  });

  afterAll(async () => {
    // Close the server and database connection
    await mongoose.connection.close();
    await server.close();
  });

  beforeEach(async () => {
    // Clear the products collection before each test
    await Product.deleteMany({});
  });

  describe('GET /api/products', () => {
    it('should get all products', async () => {
      // Create test products
      await Product.create([
        {
          name: 'Test Product 1',
          description: 'Test Description 1',
          price: 99.99,
          category: 'electronics',
          inStock: true
        },
        {
          name: 'Test Product 2',
          description: 'Test Description 2',
          price: 49.99,
          category: 'books',
          inStock: false
        }
      ]);

      const res = await request(app).get('/api/products');
      
      expect(res.statusCode).toEqual(200);
      expect(res.body.success).toBe(true);
      expect(res.body.count).toEqual(2);
      expect(Array.isArray(res.body.data)).toBe(true);
      expect(res.body.data.length).toEqual(2);
    });
  });

  describe('GET /api/products/:id', () => {
    it('should get a single product by ID', async () => {
      // Create a test product
      const product = await Product.create({
        name: 'Test Product',
        description: 'Test Description',
        price: 99.99,
        category: 'electronics',
        inStock: true
      });

      const res = await request(app).get(`/api/products/${product._id}`);
      
      expect(res.statusCode).toEqual(200);
      expect(res.body.success).toBe(true);
      expect(res.body.data._id).toBe(product._id.toString());
      expect(res.body.data.name).toBe('Test Product');
    });

    it('should return 404 if product not found', async () => {
      const nonExistentId = new mongoose.Types.ObjectId();
      const res = await request(app).get(`/api/products/${nonExistentId}`);
      
      expect(res.statusCode).toEqual(404);
      expect(res.body.success).toBe(false);
      expect(res.body.error).toBe('Product not found');
    });
  });

  describe('POST /api/products', () => {
    it('should create a new product', async () => {
      const productData = {
        name: 'New Product',
        description: 'New Description',
        price: 79.99,
        category: 'clothing',
        inStock: true
      };

      const res = await request(app)
        .post('/api/products')
        .send(productData);
      
      expect(res.statusCode).toEqual(201);
      expect(res.body.success).toBe(true);
      expect(res.body.data.name).toBe('New Product');
      expect(res.body.data.price).toBe(79.99);
      
      // Verify product was saved to database
      const savedProduct = await Product.findById(res.body.data._id);
      expect(savedProduct).not.toBeNull();
      expect(savedProduct.name).toBe('New Product');
    });

    it('should return 400 if required fields are missing', async () => {
      const invalidProductData = {
        name: 'Invalid Product',
        // Missing required fields
      };

      const res = await request(app)
        .post('/api/products')
        .send(invalidProductData);
      
      expect(res.statusCode).toEqual(400);
      expect(res.body.success).toBe(false);
    });
  });

  describe('PUT /api/products/:id', () => {
    it('should update an existing product', async () => {
      // Create a test product
      const product = await Product.create({
        name: 'Test Product',
        description: 'Test Description',
        price: 99.99,
        category: 'electronics',
        inStock: true
      });

      const updateData = {
        name: 'Updated Product',
        price: 129.99
      };

      const res = await request(app)
        .put(`/api/products/${product._id}`)
        .send(updateData);
      
      expect(res.statusCode).toEqual(200);
      expect(res.body.success).toBe(true);
      expect(res.body.data.name).toBe('Updated Product');
      expect(res.body.data.price).toBe(129.99);
      expect(res.body.data.description).toBe('Test Description'); // Unchanged field
      
      // Verify product was updated in database
      const updatedProduct = await Product.findById(product._id);
      expect(updatedProduct.name).toBe('Updated Product');
      expect(updatedProduct.price).toBe(129.99);
    });

    it('should return 404 if product not found', async () => {
      const nonExistentId = new mongoose.Types.ObjectId();
      const updateData = { name: 'Updated Product' };
      
      const res = await request(app)
        .put(`/api/products/${nonExistentId}`)
        .send(updateData);
      
      expect(res.statusCode).toEqual(404);
      expect(res.body.success).toBe(false);
      expect(res.body.error).toBe('Product not found');
    });
  });

  describe('DELETE /api/products/:id', () => {
    it('should delete an existing product', async () => {
      // Create a test product
      const product = await Product.create({
        name: 'Test Product',
        description: 'Test Description',
        price: 99.99,
        category: 'electronics',
        inStock: true
      });

      const res = await request(app).delete(`/api/products/${product._id}`);
      
      expect(res.statusCode).toEqual(200);
      expect(res.body.success).toBe(true);
      
      // Verify product was deleted from database
      const deletedProduct = await Product.findById(product._id);
      expect(deletedProduct).toBeNull();
    });

    it('should return 404 if product not found', async () => {
      const nonExistentId = new mongoose.Types.ObjectId();
      
      const res = await request(app).delete(`/api/products/${nonExistentId}`);
      
      expect(res.statusCode).toEqual(404);
      expect(res.body.success).toBe(false);
      expect(res.body.error).toBe('Product not found');
    });
  });
});
