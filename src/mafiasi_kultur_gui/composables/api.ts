import {AgsApi, Configuration, MediumsApi} from "~/utils/apiClient";

async function useApiConfig(): Promise<Configuration> {
    const appConfig = useRuntimeConfig();
    const userManager = useUserManager();

    return new Configuration({
        basePath: appConfig.public.apiBase,
        headers: {
            "Authorization": `Bearer ${(await userManager.getUser())!.access_token}`,
        }
    })
}

export async function useAgApi(): Promise<AgsApi> {
    return new AgsApi(await useApiConfig())
}

export async function useMediumApi(): Promise<MediumsApi> {
    return new MediumsApi(await useApiConfig())
}
