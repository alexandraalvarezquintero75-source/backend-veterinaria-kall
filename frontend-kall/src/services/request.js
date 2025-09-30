// Configuración de Axios
import axios from 'axios'
import { useLoadingStore } from '@/stores/loading'

const request = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json'
  }
})

export default request
// Configuración de Axios
// import axios from 'axios'
// import { useLoadingStore } from '@/stores/loading'

// const request = axios.create({
//   baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
//   headers: {
//     'Content-Type': 'application/json',
//   },
// })

// // Interceptor para requests
// request.interceptors.request.use((config) => {
//   const loadingStore = useLoadingStore()
//   loadingStore.setLoading(true)
//   return config
// })

// // Interceptor para responses
// request.interceptors.response.use(
//   (response) => {
//     const loadingStore = useLoadingStore()
//     loadingStore.setLoading(false)
//     return response
//   },
//   (error) => {
//     const loadingStore = useLoadingStore()
//     loadingStore.setLoading(false)
//     return Promise.reject(error)
//   }
// )

// export default request

