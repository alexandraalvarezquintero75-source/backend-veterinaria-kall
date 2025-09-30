<template>
  <form @submit.prevent="savePet">
    <div class="m-5">
      <!-- Fila 1 -->
      <div class="row mb-3">
        <div class="col-md-6">
          <input
            type="text"
            class="form-control"
            placeholder="Nombre de mascota"
            v-model="name"
          />
        </div>
        <div class="col-md-6">
          <select
            class="form-select"
            v-model="species"
            aria-label="Selecciona especie"
          >
            <option disabled value="">Selecciona una especie</option>
            <option
              v-for="option in speciesOptions"
              :key="option.value"
              :value="option.value"
            >
              {{ option.label }}
            </option>
          </select>
        </div>
      </div>

      <!-- Fila 2 -->
      <div class="row mb-3">
        <div class="col-md-6">
          <input
            type="text"
            class="form-control"
            placeholder="Raza"
            v-model="raza"
          />
        </div>
        <div class="col-md-6">
          <input
            type="text"
            class="form-control"
            placeholder="Sexo"
            v-model="sexo"
          />
        </div>
      </div>

      <!-- Fila 3 -->
      <div class="row mb-3">
        <div class="col-md-6">
          <Datepicker
            v-model="nacimiento"
            :enableTimePicker="false"
            class="form-control"
            placeholder="Fecha de nacimiento"
          />
        </div>
        <div class="col-md-6">
          <input
            type="text"
            class="form-control"
            placeholder="Características físicas"
            v-model="caracteristicas"
          />
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-md-6">
          <div
            class="upload-box d-flex flex-column align-items-center justify-content-center"
            @click="$refs.fileInput.click()"
          >
            <i class="bi bi-cloud-upload fs-1 text-success"></i>
            <p class="mt-2 text-muted">Haz clic o arrastra una imagen aquí</p>
            <small v-if="foto">{{ foto.name }}</small>
          </div>

          <!-- input file -->
          <input
            type="file"
            ref="fileInput"
            class="d-none"
            id="foto"
            accept="image/*"
            @change="onFileChange"
          />
        </div>

        <FormularioButtons @save="savePet" @cancel="redirecto" />
      </div>
    </div>
  </form>
</template>

<script setup>
import { ref } from "vue";
import Datepicker from "vue3-datepicker";
import FormularioButtons from "@/components/desing/atoms/FormularioButtons.vue";
import { APP_ROUTE_NAMES } from "@/constants/routeNames";
import { useRouter, useRoute } from "vue-router";
const nacimiento = ref(null);
const foto = ref(null);
const species = ref("");
const router= useRouter()
const name = ref("")
const raza = ref("")
const sexo = ref("")
const caracteristicas = ref("")

const onFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    foto.value = file;
    previewUrl.value = URL.createObjectURL(file); //  se genera la URL temporal
  }
};
const redirecto=()=>{
    router.push({name:APP_ROUTE_NAMES.PETS})
}
const speciesOptions = ref([
  { value: "perro", label: "Perro" },
  { value: "gato", label: "Gato" },
  { value: "ave", label: "Ave" },
  { value: "conejo", label: "Conejo" },
]);

const savePet= async()=>{

}
</script>
<style scoped>
/* div {
  border: 5px dashed rgba(0, 128, 0, 0.4);
} */
.upload-box {
  border: 2px dashed #198754; /* verde bootstrap */
  border-radius: 12px;
  padding: 30px;
  cursor: pointer;
  text-align: center;
  transition: background-color 0.2s ease;
}
.upload-box:hover {
  background-color: rgba(25, 135, 84, 0.05);
}
</style>
