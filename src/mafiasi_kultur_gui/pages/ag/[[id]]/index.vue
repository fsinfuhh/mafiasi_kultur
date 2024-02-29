<script lang="ts" setup>
import type {AG, MediumViewset} from "~/utils/apiClient";

definePageMeta({
  name: "ag_index",
  middleware: ["authenticated"],
})

const route = useRoute();
const agApi = await useAgApi();
const mediumApi = await useMediumApi();
const ag = ref<AG | null>(null);
const proposals = ref<MediumViewset[]>([]);

onMounted(async () => {
  ag.value = await agApi.agsRetrieve({
    id: route.params.id as string
  })
  proposals.value = await Promise.all(
      ag.value.openProposals.map((id) => mediumApi.mediumsRetrieve({
        id: id,
      }))
  )
})
</script>

<template>
  <div v-if="ag !== null">
    <h1>{{ ag.name }}</h1>
    <h2>Proposals</h2>
    <ul>
      <li v-for="proposal in proposals">{{ proposal.name }} (proposed by {{ proposal.proposal.proposedBy }})</li>
    </ul>
  </div>
</template>
