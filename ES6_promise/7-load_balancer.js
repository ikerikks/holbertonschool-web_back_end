export default async function loadBalancer(chinaDownload, USDownload) {
  const response = await Promise.race([chinaDownload, USDownload]);
  return response;
}
