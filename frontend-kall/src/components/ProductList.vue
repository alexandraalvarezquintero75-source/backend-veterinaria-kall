<template>
  <div class="p-4">
    <h1 class="text-2xl mb-4">Productos</h1>
    <button
      @click="showCreate = true"
      class="px-3 py-1 bg-blue-600 text-white rounded"
    >
      Nuevo
    </button>

    <table class="min-w-full mt-4 border">
      <thead>
        <tr>
          <th class="p-2">ID</th>
          <th class="p-2">Nombre</th>
          <th class="p-2">Precio</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in products" :key="p.id">
          <td class="p-2">{{ p.id }}</td>
          <td class="p-2">{{ p.name }}</td>
          <td class="p-2">{{ p.price }}</td>
        </tr>
      </tbody>
    </table>

    <div v-if="showCreate" class="mt-4 p-4 border rounded">
      <input v-model="form.name" placeholder="Nombre" class="border p-2 mr-2" />
      <input
        v-model.number="form.price"
        placeholder="Precio"
        type="number"
        class="border p-2 mr-2"
      />
      <button
        @click="createProduct"
        class="px-3 py-1 bg-green-600 text-white rounded"
      >
        Guardar
      </button>
      <button
        @click="showCreate = false"
        class="px-3 py-1 bg-gray-300 rounded ml-2"
      >
        Cancelar
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../services/api";

const products = ref([]);
const showCreate = ref(false);
const form = ref({ name: "", price: 0 });

onMounted(async () => {
  const res = await api.get("/products");
  products.value = res.data;
});

const createProduct = async () => {
  const res = await api.post("/products", form.value);
  products.value.push(res.data);
  showCreate.value = false;
  form.value = { name: "", price: 0 };
};
</script>
