import apiClient from './api';

export interface CartItem {
  id: number;
  product_id: number;
  quantity: number;
  price: number;
}

export interface Cart {
  id: number;
  user_id: number;
  items: CartItem[];
  total_price: number;
}

export const cartService = {
  getCart: async () => {
    const response = await apiClient.get<Cart>('/cart');
    return response.data;
  },

  addItem: async (productId: number, quantity: number) => {
    const response = await apiClient.post<Cart>('/cart/items', {
      product_id: productId,
      quantity,
    });
    return response.data;
  },

  updateItem: async (itemId: number, quantity: number) => {
    const response = await apiClient.put<Cart>(`/cart/items/${itemId}`, {
      quantity,
    });
    return response.data;
  },

  removeItem: async (itemId: number) => {
    const response = await apiClient.delete<Cart>(`/cart/items/${itemId}`);
    return response.data;
  },

  clearCart: async () => {
    const response = await apiClient.delete<Cart>('/cart');
    return response.data;
  },
};
