<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Produto extends Model
{
    use HasFactory;

    protected $fillable = ['nome', 'preco', 'quantidade', 'distribuidora_id', 'categoria_id', 'created_by'];

    // Relacionamento distribuidora
    public function distribuidora() {
        return $this->belongsTo(Distribuidora::class);
    }

    // Relacionamento categoria
    public function categoria() {
        return $this->belongsTo(Categoria::class);
    }

    // Relacionamento user
    public function createdBy() {
        return $this->belongsTo(User::class, 'created_by');
    }
}
