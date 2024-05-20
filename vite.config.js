import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path'

export default defineConfig({
  base:'./',
  publicPath: './' ,
  plugins: [vue()],
  define: {
    'process.env': {},
  },
  css: {
    preprocessorOptions: {
      scss: {
        charset: false,
        // additionalData: `@use "@/assets/styles/element/index.scss" as *;`,
      },
    },
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        pathRewrite:{'^/api':''}, //将所有含/api路径的，去掉/api转发给服务器
      }
    }
  },
  resolve: {
    // 配置路径别名
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
});