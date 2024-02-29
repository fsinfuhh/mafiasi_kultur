import {Configuration} from "~/utils/apiClient";

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

/*
 * Construct api clients like this:
 *
 * import {StuffApi} from "~/utils/apiClient";
 * export async function useStuffApi(): Promise<StuffApi> {
 *  return new StuffApi(await useApiConfig());
 * }
 */
