<template>
  <div>
    <!-- Botones generales -->
    <div class="d-flex justify-content-end mt-4 mb-3">
      <button
        class="btn btn-success rounded-circle d-flex align-items-center justify-content-center me-2"
        style="width: 40px; height: 40px; font-size: 20px"
        @click="goForm"
      >
        +
      </button>
      <AccionButtons
        v-if="clientes.length"
        :entity-id="clientes[0].id"
        @delete="handleDelete"
        @edit="handleEdit"
        @view="handleView"
        @save="goForm"
      />
      <!-- <AccionButtons
  :entity-id="clientes[0]?.id"
  @delete="handleDelete"
  @edit="handleEdit"
  @view="handleView"
/> -->
    </div>
    <InfoCard v-if="clientes.length" :client="clientes[0]" />

    <div class="p-4">
      <DataTable
        :columns="columns"
        :data="clientes"
        @update:selected="selectedClients = $event"
        @row-click="(client) => (selectedClient.value = client)"
      />
    </div>
  </div>
</template>

<script setup>
import DataTable from "@/components/desing/molecules/DataTable.vue";
import InfoCard from "./components/InfoCard.vue";
import AccionButtons from "@/components/desing/molecules/AccionButtons.vue";
import { useRouter } from "vue-router";
import { APP_ROUTE_NAMES } from "@/constants/routeNames";
import { getClients } from "@/services/clients";
import { ref, onMounted } from "vue";
import { deleteClient } from "@/services/clients";
import { useSwal } from "@/utility/useSwal";
const { showError, showConfirm, showSuccess } = useSwal();
const router = useRouter();
const selectedClients = ref([]);
const clientes = ref([]);
const goForm = () => {
  router.push({ name: APP_ROUTE_NAMES.FORM_CLIENT });
};

onMounted(() => {
  loadClients();
});
const selectedClient = ref(null);
const columns = [
  { label: "Nombre", key: "name", icon: "bi bi-person text-success" },
  { label: "Email", key: "email", icon: "bi bi-envelope text-success" },
  { label: "Teléfono", key: "telephone", icon: "bi bi-telephone text-success" },
  { label: "Dirección", key: "address", icon: "bi bi-geo-alt text-success" },
  { label: "Ciudad", key: "city", icon: "bi bi-buildings-fill text-success" },
];

const loadClients = async () => {
  try {
    const response = await getClients();
    clientes.value = response.data;
  } catch (error) {
    console.error("error al cargar clientes", error);
  }
};
const handleDelete = async (id) => {
  try {
    const confirmResult = await showConfirm(
      "¿Estás seguro de eliminar este cliente?",
      "Esta acción no se puede deshacer.",
      { iconColor: "#dc3545" }, // rojo
    );
    if (confirmResult.isConfirmed) {
      await deleteClient(id);
      await showSuccess("Cliente eliminado exitosamente");
      await loadClients();
    }
  } catch (error) {
    console.error("Error al eliminar cliente", error);
    showError("No se pudo eliminar el cliente.");
  }
};

const handleEdit = async (id) => {
  let clientId = id;

  // Si no llega un id directo (desde AccionButtons), tomamos el seleccionado en la tabla
  if (!clientId) {
    if (selectedClient.value) {
      clientId = selectedClient.value.id;
    } else if (selectedClients.value.length) {
      clientId = selectedClients.value[0].id;
    }
  }

  if (!clientId) {
    showError("Debes seleccionar un cliente para editarlo");
    return;
  }

  router.push({
    name: APP_ROUTE_NAMES.FORM_CLIENT,
    params: { id: clientId },
  });
};
</script>
