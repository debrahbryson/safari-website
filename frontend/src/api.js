import axios from 'axios'

const api = axios.create({ baseURL: '/api' })

export const getTours = (params) => api.get('/tours', { params })
export const getTour = (slug) => api.get(`/tours/${slug}`)
export const createBooking = (data) => api.post('/bookings', data)

export default api
