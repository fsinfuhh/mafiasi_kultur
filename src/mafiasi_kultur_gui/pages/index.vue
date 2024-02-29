<script lang="ts" setup>
import {useAgApi} from "~/composables/api";
import type {AG} from "~/utils/apiClient";

definePageMeta({
  name: "index",
  middleware: ["authenticated"],
})
useSeoMeta({
  title: "Mafiasi Kulturgenießer"
})

const agApi = await useAgApi();
const ags = ref<AG[]>([]);

onMounted(async () => {
  ags.value = await agApi.agsList();
});
</script>

<template>
  <div>
    <ul>
      <li v-for="ag in ags">
        <NuxtLink :to="{ name: 'ag_index', params: { id: ag.id } }">{{ ag.name }}</NuxtLink>
      </li>
    </ul>
  </div>
</template>
