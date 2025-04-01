<template>
    <div>
      <h1>Busca de Operadoras</h1>
      <input type="text" v-model="searchTerm" placeholder="Digite o nome da operadora..." />
      <button @click="performSearch">Buscar</button>
  
      <div v-if="loading">Carregando...</div>
      <div v-if="error">{{ error }}</div>
  
      <div v-if="results.length > 0">
        <ul>
          <li v-for="item in results" :key="item.Registro_">
            {{ item.Nome_Fan }} - {{ item.CNPJ }}
          </li>
        </ul>
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
        error: null,
      };
    },
    methods: {
      async performSearch() {
        this.loading = true;
        this.error = null;
        try {
          const response = await fetch(`https://intuitivecare4.onrender.com/api/search?q=${encodeURIComponent(this.searchTerm)}`);
          if (!response.ok) throw new Error('Erro na API');
          this.results = await response.json();
        } catch (err) {
          this.error = 'Erro ao buscar dados. Tente novamente.';
        } finally {
          this.loading = false;
        }
      }
    }
  };
  </script>