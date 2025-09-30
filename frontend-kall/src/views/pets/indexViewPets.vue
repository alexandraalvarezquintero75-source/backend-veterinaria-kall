<template>
  <div class="container-fluid">
    <!-- Header + Botones de acción -->
    <div
      class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3"
    >
      <!-- Logo + Título -->
      <TitleHeader title="Mascotas" position="start" color="text-success">
        <template #icon-header>
          <div class="d-flex align-items-center gap-2">
            <img
              src="@/assets/logoMascotas.png"
              alt="Logo"
              class="img-fluid"
              style="max-width: 60px"
            />
            <NewGoalIcon width="40" height="40" />
          </div>
        </template>
      </TitleHeader>

      <!-- Botones de acción -->
      <div class="d-flex flex-wrap gap-2">
        <AccionButtons
          @save="goForm"
        />
      </div>
    </div>

    <!-- Filtros e Inputs -->
    <div class="row g-3 mb-3">
      <!-- Buscador -->
      <div class="col-12 col-md-4">
        <div class="card bg-white p-4 shadow-sm rounded h-100">
          <div class="input-group">
            <input
              type="search"
              class="form-control"
              placeholder="Filtrar"
              aria-label="Search"
              aria-describedby="search-addon"
            />
            <span class="input-group-text border-0" id="search-addon">
              <i class="bi bi-search text-success"></i>
            </span>
          </div>
        </div>
      </div>

      <!-- Información -->
      <div class="col-12 col-md-8">
        <div class="card bg-white p-4 shadow-sm rounded h-100 w-50">
          <h5 class="card-title mb-3">{{ titulo }}</h5>

          <div class="card-text mb-2" v-for="(valor, key) in datos" :key="key">
            <strong>{{ key }}:</strong> {{ valor }}
          </div>

          <div class="mt-3">
            <button class="btn btn-success btn-sm me-2" @click="editar">
              Editar
            </button>
            <button class="btn btn-outline-secondary btn-sm" @click="verMas">
              Ver más
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import AccionButtons from "@/components/desing/molecules/AccionButtons.vue";
import TitleHeader from "@/components/desing/molecules/TitleHeader.vue";
import { useRouter } from "vue-router";
import { APP_ROUTE_NAMES } from "@/constants/routeNames";

const router = useRouter();
const goForm = () => {
  router.push({ name: APP_ROUTE_NAMES.FORM_PETS });
};
</script>

<style scoped>
.form-control:focus {
  border-color: #28a745 !important;
  box-shadow: 0 0 0 0.25rem rgba(40, 167, 69, 0.25) !important;
}
</style>
