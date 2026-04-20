import apiClient from './api';

export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  stock: number;
  image_url?: string;
}

export const productService = {
  getAll: async (skip = 0, limit = 10) => {
    const response = await apiClient.get<Product[]>('/products', {
      params: { skip, limit },
    });
    return response.data;
  },

  getById: async (id: number) => {
    const response = await apiClient.get<Product>(`/products/${id}`);
    return response.data;
  },

  search: async (query: string) => {
    const response = await apiClient.get<Product[]>('/products/search', {
      params: { q: query },
    });
    return response.data;
  },
};
