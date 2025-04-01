<template>
    <div class="search-container">
      <h2>Busca de Operadoras de Saúde</h2>
      <input 
        type="text" 
        v-model="searchTerm" 
        placeholder="Digite nome da operadora..." 
      />
      <button @click="performSearch">Buscar</button>
  
      <div v-if="loading">Carregando...</div>
      <div v-if="error">{{ error }}</div>
  
      <div v-if="results.length > 0">
        <div v-for="item in results" :key="item.Registro_ANS">
          <h3>{{ item.Nome_Fantasia }}</h3>
          <p><strong>Razão Social:</strong> {{ item.Razao_Social }}</p>
          <p><strong>CNPJ:</strong> {{ item.CNPJ }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchTerm: '',
        results: [],
        loading: false,
        error: null
      };
    },
    methods: {
      async performSearch() {
        this.loading = true;
        this.error = null;
        try {
          const response = await fetch(`https://intuitivecare-backend.onrender.com/api/search?q=${encodeURIComponent(this.searchTerm)}`);
          if (!response.ok) throw new Error('Erro na requisição.');
          this.results = await response.json();
        } catch (err) {
          this.error = 'Erro ao buscar dados.';
        } finally {
          this.loading = false;
        }
      }
    }
  };
  </script>
  
  <style>
  /* Ajuste de estilos */
  </style>