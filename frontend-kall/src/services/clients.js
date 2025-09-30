// src/services/clients.js
import request from '@/services/request'

// Crear cliente
export const createClient = (data) => {
  return request({
    url: '/v1/client/caut',
    method: 'POST',
    data
  })
}

// Listar clientes
export const getClients = (params = {}) => {
  return request({
    url: '/v1/client/gaut',
    method: 'GET',
    params
  })
}

// Obtener cliente por ID
export const getClientById = (id) => {
  return request({
    url: `/v1/client/gaut/${id}`,
    method: 'GET'
  })
}

// Actualizar cliente
export const updateClient = (id, data) => {
  return request({
    url: `/v1/client/uaut/${id}`,
    method: 'PUT',
    data
  })
}

// Eliminar cliente
export const deleteClient = (id) => {
  return request({
    url: `/v1/client/daut/${id}`,
    method: 'DELETE'
  })
}
