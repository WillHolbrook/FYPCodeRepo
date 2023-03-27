import axios from "axios";
// eslint-disable-next-line no-unused-vars -- unnecessary variable of React is needed to define as component
import React from "react";

export let axapi = axios.create({
  baseURL: process.env.REACT_APP_BASE_URL
    ? process.env.REACT_APP_BASE_URL
    : "/",
  timeout: 10000,
  headers: { "Content-Type": "application/json" },
});

export class API {
  static loginUser(body) {
    return axapi.post("auth/", body, {
      headers: {
        Authorization: null,
      },
    });
  }

  static registerUser(body) {
    return axapi.post("api/users/", body, {
      headers: {
        Authorization: null,
      },
    });
  }

  static uploadReport(reportFile) {
    let formData = new FormData();
    formData.append("uploaded_report", reportFile);
    return axapi.post("api/report_upload/", formData, {
      timeout: 3 * 60 * 1000,
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  }

  static listReports() {
    return axapi.get("api/reports/");
  }

  static getReport(report_id) {
    return axapi.get(`api/reports/${report_id}/`);
  }

  static deleteReport(report_id) {
    return axapi.delete(`api/reports/${report_id}/`);
  }

  static extractSentences(report_id) {
    return axapi.post(`api/report_extract_sentence/${report_id}/`, null, {
      timeout: 3 * 60 * 1000,
    });
  }

  static retrieveSentences(report_id, limit = 10, offset = 0) {
    return axapi.get(
      `api/report_extract_sentence/${report_id}/?limit=${limit}&offset=${offset}`
    );
  }

  static extractSentencesBERT(report_id) {
    return axapi.post(`api/report_extract_sentence_bert/${report_id}/`, null, {
      timeout: 3 * 60 * 1000,
    });
  }

  static getProfileDetails() {
    return axapi.get(`api/profile/`);
  }

  static updateProfileDetails(profileImage) {
    let formData = new FormData();
    formData.append("profile_image", profileImage);
    return axapi.post("api/profile/", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  }

  static listUsers() {
    return axapi.get(`api/users/`);
  }

  static getCurrentUser() {
    return axapi.get(`api/user/`);
  }

  static updateCurrentUserPassword(password) {
    return axapi.put(`api/user/`, { password });
  }

  static getSpecificUser(user_id) {
    return axapi.get(`api/users/${user_id}/`);
  }
}
