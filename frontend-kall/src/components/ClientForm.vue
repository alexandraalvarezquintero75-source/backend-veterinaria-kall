<template>
  <div class="card shadow-sm w-50 mx-auto mt-4">
    <div class="card-body">
      <h2 class="h5 fw-bold mb-3">Registrar Cliente</h2>

      <div class="mb-3">
        <label for="fullName" class="form-label">Nombre completo:</label>
        <input
          v-model="form.full_name"
          type="text"
          class="form-control"
          id="fullName"
          placeholder="Ej. Ana Pérez"
        />
      </div>

      <div class="mb-3">
        <label for="email" class="form-label">Email:</label>
        <input
          v-model="form.email"
          type="email"
          class="form-control"
          id="email"
          placeholder="ejemplo@correo.com"
        />
      </div>

      <button @click="saveClient" class="btn btn-success w-100">Guardar</button>

      <div v-if="message" class="alert alert-success mt-3">
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { createClient } from "@/services/clients";

const form = ref({ full_name: "", email: "" });
const message = ref("");

const saveClient = async () => {
  try {
    const res = await createClient(form.value);
    message.value = `Cliente "${res.full_name}" creado con éxito! (ID: ${res.id})`;
    form.value = { full_name: "", email: "" };
  } catch (error) {
    message.value = error.message || "Error al crear cliente";
    console.error(error);
  }
};
</script>
