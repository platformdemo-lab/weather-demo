@Library('platform-pipelines') _

withCredentials([
  string(credentialsId: 'weather-api-key', variable: 'API_KEY')
]) {

  pythonService(
    appName: "weather-service",
    port: "5000",
    envVars: [
      "API_KEY": API_KEY
    ],
    runTests: true,
    runCodeScan: true,
    runContainerScan: true
  )
}