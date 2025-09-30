<!-- InfoCard.vue -->
<template>
  <div class="container mt-4">
    <!-- Card -->
    <div class="card border-success mb-3 mx-5 mt-3" style="width: 18rem">
      <img src="..." class="card-img-top" alt="Foto cliente" />
      <div class="card-body py-3">
        <h5 class="card-title text-success">{{ client.name }}</h5>
        <p class="card-text">Información del cliente</p>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">
          <strong>Teléfono:</strong> {{ client.telephone }}
        </li>
        <li class="list-group-item">
          <strong>Correo:</strong> {{ client.email }}
        </li>
        <li class="list-group-item">
          <strong>Ciudad:</strong> {{ client.city }}
        </li>
      </ul>
      <div class="card-body">
        <button type="button" class="btn btn-outline-success">Detalles</button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  client: {
    type: Object,
    required: true,
  },
});
</script>
