@Library('platform-pipelines') _

withCredentials([
  string(credentialsId: 'weather-api-key', variable: 'API_KEY')
]) {

  pythonservice(
    appName: "weather-service",
    port: "5000",
    envVars: [
      "API_KEY": API_KEY
    ]
  )
}