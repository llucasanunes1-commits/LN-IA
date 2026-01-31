# 📱 LN IA - Gerar APK

## 🎯 3 Métodos para transformar em APK

---

## ✨ MÉTODO 1: PWA Builder (Mais Fácil - Recomendado)

### Passo a passo:

1. **Hospedar os arquivos:**
   - Suba os arquivos (index.html, manifest.json, sw.js) para um servidor com HTTPS
   - Opções gratuitas: 
     - Netlify (netlify.com)
     - Vercel (vercel.com)
     - GitHub Pages (pages.github.com)
     - Firebase Hosting (firebase.google.com)

2. **Gerar APK:**
   - Acesse: https://www.pwabuilder.com
   - Cole a URL do seu site
   - Clique em "Start"
   - Clique em "Package For Stores"
   - Escolha "Android"
   - Configure (deixe as opções padrão)
   - Clique em "Generate"
   - Baixe o APK!

### ✅ Vantagens:
- Muito fácil e rápido
- Não precisa instalar nada
- APK pronto em minutos
- Suporta atualizações automáticas

---

## 🔧 MÉTODO 2: Apache Cordova (Mais Controle)

### Pré-requisitos:
```bash
# Instalar Node.js (nodejs.org)
# Instalar Cordova
npm install -g cordova

# Instalar Android Studio (developer.android.com/studio)
```

### Passo a passo:

1. **Criar projeto Cordova:**
```bash
cordova create lnai com.lnai.app "LN IA"
cd lnai
```

2. **Adicionar plataforma Android:**
```bash
cordova platform add android
```

3. **Copiar seus arquivos:**
```bash
# Copiar index.html para www/
# Copiar manifest.json para www/
# Copiar sw.js para www/
```

4. **Adicionar plugins necessários:**
```bash
cordova plugin add cordova-plugin-media-capture
cordova plugin add cordova-plugin-device
```

5. **Editar config.xml:**
```xml
<preference name="permissions" value="none"/>
<feature name="Microphone">
    <param name="android-package" value="org.apache.cordova.media.AudioHandler" />
</feature>
```

6. **Build APK:**
```bash
cordova build android --release
```

7. **APK gerado em:**
```
platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk
```

### ✅ Vantagens:
- Mais controle sobre o app
- Acesso a recursos nativos
- Personalização avançada

---

## 🚀 MÉTODO 3: Capacitor (Moderno)

### Pré-requisitos:
```bash
npm install -g @capacitor/cli @capacitor/core
```

### Passo a passo:

1. **Inicializar Capacitor:**
```bash
npm init
npm install @capacitor/core @capacitor/cli
npx cap init
```

2. **Adicionar Android:**
```bash
npm install @capacitor/android
npx cap add android
```

3. **Copiar arquivos para pasta web:**
```bash
# Criar pasta www/ e copiar index.html, manifest.json, sw.js
```

4. **Configurar capacitor.config.json:**
```json
{
  "appId": "com.lnai.app",
  "appName": "LN IA",
  "webDir": "www",
  "bundledWebRuntime": false
}
```

5. **Sincronizar e abrir Android Studio:**
```bash
npx cap sync
npx cap open android
```

6. **No Android Studio:**
   - Build → Generate Signed Bundle / APK
   - Escolha APK
   - Create new keystore
   - Build Release

### ✅ Vantagens:
- Tecnologia moderna
- Boa performance
- Fácil manutenção

---

## 🎨 Criar Ícones do App

Use estas ferramentas para gerar ícones:

1. **Canva** (canva.com)
   - Template: 512x512px
   - Fundo verde (#00ff66)
   - Texto "LN" preto

2. **Icon Kitchen** (icon.kitchen)
   - Upload sua imagem
   - Gera todos os tamanhos automaticamente

3. **Android Asset Studio**
   - https://romannurik.github.io/AndroidAssetStudio/

### Tamanhos necessários:
- 192x192 (icon-192.png)
- 512x512 (icon-512.png)

---

## 📝 Checklist antes de publicar:

- [ ] Testar em diferentes dispositivos Android
- [ ] Verificar permissões (microfone)
- [ ] Testar modo offline
- [ ] Verificar orientação (portrait)
- [ ] Testar reconhecimento de voz
- [ ] Verificar salvamento de histórico
- [ ] Testar configurações de API

---

## 🏪 Publicar na Google Play Store:

1. **Criar conta de desenvolvedor:**
   - https://play.google.com/console
   - Taxa única: $25 USD

2. **Preparar materiais:**
   - Screenshots (mínimo 2)
   - Ícone 512x512
   - Banner 1024x500
   - Descrição do app
   - Política de privacidade

3. **Upload do APK:**
   - Create Application
   - Upload APK
   - Preencher detalhes
   - Submit for review

---

## 🆘 Troubleshooting:

**Erro: "App not installed"**
- Desinstale versão antiga primeiro
- Verifique se é APK assinado

**Microfone não funciona:**
- Adicionar permissão no AndroidManifest.xml
- Verificar se app tem permissão nas configurações

**App não abre:**
- Verificar logs: `adb logcat`
- Testar em modo debug primeiro

---

## 💡 Dicas Extras:

1. **Teste primeiro como PWA:**
   - Abra no Chrome mobile
   - Menu → "Adicionar à tela inicial"
   - Teste todas as funcionalidades

2. **Use emulador Android:**
   - Android Studio → AVD Manager
   - Teste antes de gerar APK final

3. **Versioning:**
   - Sempre incremente a versão no manifest/config
   - Mantenha changelog das mudanças

---

## 📧 Suporte:

Se tiver dúvidas, consulte:
- Documentação PWABuilder: https://docs.pwabuilder.com
- Documentação Cordova: https://cordova.apache.org/docs
- Documentação Capacitor: https://capacitorjs.com/docs

---

**🎉 Boa sorte com seu app!**
