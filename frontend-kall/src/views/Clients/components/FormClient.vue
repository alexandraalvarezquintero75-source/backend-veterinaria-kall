<template>
  <form @submit.prevent="saveClient">
    <div class="m-5">
      <div class="row g-3 mb-3">
        <div class="col-md-6">
          <input
            type="text"
            class="form-control"
            placeholder="Nombre"
            v-model="client.name"
          />
        </div>
        <div class="col-md-6">
          <input
            type="email"
            class="form-control"
            placeholder="Correo"
            v-model="client.email"
          />
        </div>

        <div class="row g-3 mb-3">
          <div class="col-md-4">
            <input
              type="text"
              class="form-control"
              placeholder="Teléfono"
              v-model="client.telephone"
            />
          </div>
          <div class="col-md-4">
            <input
              type="text"
              class="form-control"
              placeholder="Dirección"
              v-model="client.address"
            />
          </div>
          <div class="col-md-4">
            <input
              type="text"
              class="form-control"
              placeholder="Ciudad"
              v-model="client.city"
            />
          </div>
        </div>

        <!-- Textarea -->
        <div class="mb-3">
          <textarea
            class="form-control"
            rows="3"
            placeholder="Descripción"
            v-model="client.description"
          ></textarea>
        </div>

        <FormularioButtons @save="saveClient" @cancel="redirecto" />
      </div>
    </div>
  </form>
</template>

<script setup>
import FormularioButtons from "@/components/desing/atoms/FormularioButtons.vue";
import { APP_ROUTE_NAMES } from "@/constants/routeNames";
import { reactive, onMounted, ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import { createClient, getClientById, updateClient } from "@/services/clients";
import { useSwal } from "@/utility/useSwal";

const { showError, showConfirm, showSuccess } = useSwal();
const router = useRouter();
const route = useRoute();

const client = reactive({
  name: "",
  email: "",
  telephone: "",
  address: "",
  city: "",
  description: "",
});

const isEdit = ref(false);
const clientId = ref(null);

onMounted(async () => {
  if (route.params.id) {
    isEdit.value = true;
    clientId.value = route.params.id;
    try {
      const { data } = await getClientById(clientId.value);
      Object.assign(client, data); // rellenar el formulario con los datos
    } catch (err) {
      console.error("Error al cargar cliente", err);
      showError("No se pudo cargar la información del cliente");
    }
  }
});

const redirecto = () => {
  router.push({ name: APP_ROUTE_NAMES.CLIENTS });
};

const saveClient = async () => {
  try {
    if (isEdit.value) {
      await updateClient(clientId.value, client);
      await showSuccess("Cliente actualizado con éxito");
    } else {
      await createClient(client);
      await showSuccess("Cliente creado con éxito");
    }
    redirecto();
  } catch (err) {
    console.error("Error al guardar cliente", err);
    showError("No se pudo guardar el cliente");
  }
};
</script>

<style scoped>
.form-control:focus {
  border-color: #28a745 !important;
  box-shadow: 0 0 0 0.25rem rgba(40, 167, 69, 0.25) !important;
}
</style>
