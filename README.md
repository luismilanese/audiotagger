# AudioTagger CLI

[![Python 3.14+](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/)
[![Built with uv](https://img.shields.io/badge/built%20with-uv-purple.svg)](https://github.com/astral-sh/uv)

*[English version below](#english-version)*

---

## 🇧🇷 Português

**AudioTagger** é uma ferramenta de linha de comando (CLI) em Python para leitura de metadados de arquivos de áudio e renomeação em lote baseada em máscaras dinâmicas e customizáveis.

Construído com uma arquitetura **MVC Adaptada para CLI**, isolando regras de negócio, extração de metadados e apresentação no terminal.
Construído com uma arquitetura **MVC Adaptada para CLI**, desacoplando regras de negócio, extração multi-formato de metadados e apresentação no terminal.

---

### 🚀 Funcionalidades

- **Suporte Multi-formato:** Suporta arquivos **MP3** (`.mp3`), **OGG** (`.ogg` — Vorbis, Opus, etc.) e **FLAC** (`.flac`).
- **Seguro por Padrão (*Safe by Default*):** O modo de simulação (*Preview*) é ativado por padrão. Nenhum arquivo é renomeado sem a confirmação explícita (`--apply`).
- **Motor de Máscaras Dinâmico:** Suporte a marcadores intuitivos como `%artist%`, `%title%`, `%album%`, `%track_number%` e `%year%`.
- **Sanitização de Nomes:** Remove automaticamente caracteres proibidos pelo sistema operacional (`/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`).
- **Processamento Individual ou em Lote:** Aceita o caminho para um único arquivo `.mp3` ou uma pasta inteira.
- **Interface Terminal Colorida:** Exibição clara e formatada com cores ANSI indicando arquivos alterados, erros e sumário final.
- **Sanitização de Nomes:** Remove automaticamente caracteres proibidos pelo sistema operacional (`/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`) e trata pontos finais no nome.
- **Processamento Individual ou em Lote:** Aceita o caminho para um único arquivo de áudio ou um diretório inteiro.
- **Validação e Tratamento Robusto de Erros:** Identifica caminhos inexistentes, colisões de nomes de arquivos, arquivos sem suporte e diretórios vazios.
- **Interface Terminal Colorida:** Exibição clara e formatada com cores ANSI indicando arquivos alterados, erros, avisos e sumário final de execução.

---

### 📦 Instalação e Requisitos

- Python `>= 3.14`
- [uv](https://github.com/astral-sh/uv) (recomendado) ou `pip`

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/luismilanese/audiotagger.git
cd audiotagger
uv sync
```

---

### 💻 Como Usar

#### 1. Simulação com Máscara Padrão (Preview)
Por padrão, a ferramenta apenas simula a renomeação usando a máscara `"%artist% - %track_number% - %title%"`:
```bash
uv run audiotagger test_files
```

#### 2. Simulação com Máscara Customizada
Use a opção `-m` ou `--mask` para definir sua própria estrutura:
```bash
uv run audiotagger test_files -m "%track_number% ~ %artist% ~ %title%"
```

#### 3. Aplicar as Alterações no Disco
Para de fato renomear os arquivos físicos, passe a flag `-a` ou `--apply`:
```bash
uv run audiotagger test_files -m "%track_number% ~ %artist% ~ %title%" --apply
```

#### 4. Renomear um Único Arquivo
```bash
uv run audiotagger "test_files/1 - Revelation in Sin.mp3" -m "%artist% - %title%" --apply
```

---

### 🏷️ Marcadores Suportados (Tags)

| Marcador | Descrição |
| :--- | :--- |
| `%artist%` | Nome do Artista |
| `%title%` | Título da Música |
| `%album%` | Nome do Álbum |
| `%track_number%` | Número da Faixa (sem contagem total, ex: `01`) |
| `%track_number%` | Número da Faixa (normalizado, ex: `01`) |
| `%year%` | Ano de Lançamento |

---

### ⚙️ Opções da Linha de Comando

```text
usage: audiotagger [-h] [-m MASK] [-a] path

positional arguments:
  path                  Caminho para o arquivo ou diretório de áudio
  path                  location of the file or folder

options:
  -h, --help            Exibe a mensagem de ajuda e encerra
  -m, --mask MASK       Máscara para renomeação (padrão: %artist% - %track_number% - %title%)
  -a, --apply           Aplica e grava as alterações no disco (desativa o modo preview)
  -h, --help            show this help message and exit
  -m, --mask MASK       mask pattern files will be renamed to (default: %artist% - %track_number% - %title%)
  -a, --apply           write the changes to disk
```

---

<br>

## 🇬🇧 English Version

**AudioTagger** is a lightweight Python CLI utility for reading audio file metadata and batch-renaming files based on customizable token masks.
**AudioTagger** is a lightweight Python CLI utility for reading audio metadata and batch-renaming files based on customizable token masks.

Engineered following an **adapted MVC architecture for CLI applications**, ensuring full decoupling between domain business logic, metadata extraction adapters, and terminal presentation.
Engineered following an **adapted MVC architecture for CLI applications**, ensuring clean separation of concerns between domain models, multi-format metadata extraction, and terminal presentation.

---

### 🚀 Key Features

- **Safe by Default:** Dry-run / Preview mode is active by default. No files are renamed without explicit confirmation (`--apply`).
- **Dynamic Token Mask Engine:** Flexible template placeholders like `%artist%`, `%title%`, `%album%`, `%track_number%`, and `%year%`.
- **Filesystem-Safe Sanitization:** Prohibited operating system characters (`/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`) are safely stripped/normalized.
- **Batch or Single-File Processing:** Accepts a path to a specific `.mp3` file or an entire directory.
- **ANSI Color Output:** Formatted terminal reports highlighting successes, collisions/errors, and summary counts.
- **Multi-format Support:** Seamlessly handles **MP3** (`.mp3`), **OGG** (`.ogg` — Vorbis, Opus, etc.), and **FLAC** (`.flac`) files.
- **Safe by Default:** Dry-run / Preview mode is active by default. No files are altered on disk without explicit confirmation (`--apply`).
- **Dynamic Token Mask Engine:** Flexible template placeholders such as `%artist%`, `%title%`, `%album%`, `%track_number%`, and `%year%`.
- **Filesystem-Safe Sanitization:** Prohibited operating system characters (`/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`) and trailing dots are safely sanitized.
- **Batch or Single-File Processing:** Accepts a path to a specific audio file or an entire directory.
- **Robust Error Handling & Validation:** Catches non-existent paths, file name collisions, unsupported formats, and empty directories.
- **ANSI Color Output:** Clean terminal output highlighting modified files, errors, warnings, and summary statistics.

---

### 📦 Installation & Setup

- Python `>= 3.14`
- [uv](https://github.com/astral-sh/uv) (recommended) or `pip`

Clone the repository and synchronize dependencies:

```bash
git clone https://github.com/luismilanese/audiotagger.git
cd audiotagger
uv sync
```

---

### 💻 Usage Examples

#### 1. Dry-Run with Default Mask (Preview Mode)
By default, the tool performs a safe preview using `"%artist% - %track_number% - %title%"`:
```bash
uv run audiotagger test_files
```

#### 2. Dry-Run with Custom Mask
Use `-m` or `--mask` to specify your pattern:
```bash
uv run audiotagger test_files -m "%track_number% ~ %artist% ~ %title%"
```

#### 3. Apply Changes to Disk
Pass the `-a` or `--apply` flag to commit file renames:
```bash
uv run audiotagger test_files -m "%track_number% ~ %artist% ~ %title%" --apply
```

#### 4. Rename a Single File
```bash
uv run audiotagger "test_files/1 - Revelation in Sin.mp3" -m "%artist% - %title%" --apply
```

---

### 🏷️ Supported Placeholders

| Placeholder | Description |
| :--- | :--- |
| `%artist%` | Artist Name |
| `%title%` | Track Title |
| `%album%` | Album Name |
| `%track_number%` | Track Number (normalized, e.g. `01`) |
| `%year%` | Release Year |

---

### ⚙️ CLI Reference

```text
usage: audiotagger [-h] [-m MASK] [-a] path

positional arguments:
  path                  Location of the audio file or folder
  path                  location of the file or folder

options:
  -h, --help            Show this help message and exit
  -m, --mask MASK       Mask pattern files will be renamed to (default: %artist% - %track_number% - %title%)
  -a, --apply           Write the changes to disk (disables preview mode)
  -h, --help            show this help message and exit
  -m, --mask MASK       mask pattern files will be renamed to (default: %artist% - %track_number% - %title%)
  -a, --apply           write the changes to disk
```

