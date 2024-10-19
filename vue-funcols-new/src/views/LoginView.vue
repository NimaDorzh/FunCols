<template>
  <div class="login">
    <h2>Вход</h2>
    <form @submit.prevent="login" class="form-container">
      <div class="form-group">
        <label for="username">Имя пользователя:</label>
        <input v-model="username" type="text" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="password">Пароль:</label>
        <input v-model="password" type="password" class="form-control" required />
      </div>
      <button type="submit" class="btn btn-primary">Войти</button>
    </form>
    <p v-if="error" class="error-message">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: null,  // Добавлена переменная для хранения ошибок
    };
  },
  
  methods: {
    login() {
      axios.post('http://localhost:8000/api/users/login/', {  // Убедитесь, что URL верный
        username: this.username,
        password: this.password,
      })
      .then(response => {
        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        alert('Вход успешен!');
        // Здесь можно перенаправить пользователя на главную страницу
      })
      .catch(error => {
        // Проверка на существование сообщения об ошибке
        if (error.response && error.response.data) {
          this.error = error.response.data.detail || 'Ошибка входа';  // Используйте свойство detail или общее сообщение
        } else {
          this.error = 'Ошибка сети';
        }
      });
    }
  }
};
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.form-container {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  font-weight: bold;
  margin-bottom: 5px;
  display: block;
}

.form-control {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  box-sizing: border-box;
}

.btn {
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 10px;
}
</style>
