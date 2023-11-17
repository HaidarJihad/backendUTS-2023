<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PatientController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

// method GET
Route::get('/patients', [PatientController::class, 'index']);

// method POST
Route::POST('/patients', [PatientController::class, 'store']);

// method GET
Route::get('/patients/{id}', [PatientController::class, 'show']);

// method PUT
Route::put('/patients/{id}', [PatientController::class, 'update']);

// method DELETE
Route::delete('/patients/{id}', [PatientController::class, 'destroy']);

// method GET
Route::get('/patients/search/{name}', [PatientController::class, 'search']);

// method GET
Route::get('/patients/status/positive', [PatientController::class, 'positive']);

// method GET
Route::get('/patients/status/recovered', [PatientController::class, 'recovered']);

// method GET
Route::get('/patients/status/dead', [PatientController::class, 'dead']);

// route Auth method post
Route::post('/register', [AuthController::class, 'register']);
Route::post('/login', [AuthController::class, 'login']);