# Voice Lead Demo

A simple Persian voice processing pipeline using FastAPI, local Whisper, and n8n.

## Overview

This project receives a Persian voice file, converts it to text using local Whisper, extracts basic lead information, and returns the structured result.

## Workflow

Voice File → n8n Webhook → FastAPI → Faster-Whisper → Lead Extraction → Google Sheets

## Features

- Persian speech-to-text
- Local Faster-Whisper inference
- FastAPI REST API
- Basic lead information extraction
- n8n integration
- Google Sheets integration

## Extracted Fields

- `project_type`
- `need`
- `timeline`
- `budget`
- `raw_text`

## Technologies

- Python
- FastAPI
- Faster-Whisper
- n8n
- Google Sheets
- Git / GitHub

## Note

This repository is a demonstration MVP focused on the core voice-processing workflow. The extraction rules can be extended or replaced with an AI API for more advanced text understanding.
