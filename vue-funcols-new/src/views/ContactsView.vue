<template>
  <div class="contacts">
    <h1>Contact Us</h1>
    
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name:</label>
        <input
          type="text"
          v-model="contact.name"
          id="name"
          required
          placeholder="Enter your name"
        />
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input
          type="email"
          v-model="contact.email"
          id="email"
          required
          placeholder="Enter your email"
        />
      </div>

      <div class="form-group">
        <label for="message">Message:</label>
        <textarea
          v-model="contact.message"
          id="message"
          required
          placeholder="Your message"
        ></textarea>
      </div>

      <button type="submit">Send</button>
    </form>
    
    <div v-if="submitted" class="confirmation">
      <p>Thank you for your message, {{ contact.name }}! We will get back to you soon.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      contact: {
        name: "",
        email: "",
        message: ""
      },
      submitted: false
    };
  },
  methods: {
    submitForm() {
      if (this.contact.name && this.contact.email && this.contact.message) {
        this.submitted = true;

        // Here, you can also send the data to a server via an API
        // axios.post('/api/contact', this.contact)
        //   .then(response => {
        //     // Handle success
        //   })
        //   .catch(error => {
        //     // Handle error
        //   });

        // Clear form after submission
        this.contact.name = "";
        this.contact.email = "";
        this.contact.message = "";
      }
    }
  }
};
</script>

<style scoped>
.contacts {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

input,
textarea {
  width: 100%;
  padding: 10px;
  margin: 5px 0;
}

button {
  padding: 10px 20px;
  background-color: #007BFF;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.confirmation {
  margin-top: 20px;
  background-color: #e0ffe0;
  padding: 10px;
  border: 1px solid #00b300;
}
</style>
